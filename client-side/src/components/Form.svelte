<script>
    import { onMount, onDestroy, createEventDispatcher, afterUpdate } from "svelte";

    // bind the passed state from Contact component to the form
    // element in this Form component
    export let form;

    let countries = [];
    let model_names = ['------------------------'];

    let first_name = "";
    let last_name = "";
    let email_address = "";
    let country_code = "";
    let model_name = "";

    let mobile_num = "";
    const phone_reg = `[0-9]{'{'}3{'}'}-[0-9]{'{'}3{'}'}-[0-9]{'{'}4{'}'}`;

    let message = "";
    let prompt = "";
    let temperature = 1.0;
    let seq_len = 250;
    let images = null;

    let dispatch = createEventDispatcher();

    const get_country_codes = async () => {
        try{
            const url = 'https://gist.githubusercontent.com/anubhavshrimal/75f6183458db8c453306f93521e93d37/raw/f77e7598a8503f1f70528ae1cbf9f66755698a16/CountryCodes.json';
            const response = await fetch(url);

            if(response.status === 200){
                console.log("retrieval successful");

                const data = await response.json();

                // returned data list consists of dictionaries containing
                // keys name, dial_code, and code e.g. 'Afghanistan', '+93', 'AF'
                countries = [...data];

                // on mount set state of country code to dial code of first country
                country_code = countries[0]['dial_code'];
                // console.table(countries);

            }else{
                console.log(`retrieval unsuccessful. Response status ${response.status} occured`)
            }    

        }catch(error){
            console.log(`Server access denied. Error '${error}' occured`);
        }
    };

    const get_model_names = async () => {
        try{
            const url = 'http://127.0.0.1:5000/model-names';
            const response = await fetch(url);

            if(response.status === 200){
                console.log("retrieval successful");

                const data = await response.json();

                // returned data consists of key value pairs 
                // particularly the model_names and the list of names
                model_names = [...data['model_names']];

                // on mount set state of model_name to 
                // first model_name in model_names list
                model_name = model_names[0];

            }else{
                console.log(`retrieval unsuccessful. Response status ${response.status} occured`)
            }

        }catch(error){
            console.log(`Server access denied. Error '${error}' occured`);
        }
        
    }

    onMount(async () => {
        get_country_codes();
        get_model_names();
    });

    afterUpdate(async () => {
        console.log(images);
    })

    const handle_submit = (event) => {
        const mail = {
            first_name: first_name,
            last_name: last_name,
            email_address: email_address,
            country_code: country_code,
            mobile_num: mobile_num,
            message: message
        };

        dispatch('sendData', mail);
    };

    
</script>

<form class="form one-col" on:submit|preventDefault={handle_submit} method="post" bind:this={form}>
    <div class="fname-container">
        <label for="first-name" class="fname-label">First name</label>
        <input type="text" name="first_name" id="first-name" class="fname-field" placeholder="John Smith" bind:value={first_name}/>
    </div>
    <div class="lname-container">
        <label for="last-name" class="lname-label">Last name</label>
        <input type="text" name="last_name" id="last-name" class="lname-field" placeholder="Meyer" bind:value={last_name}/>
    </div>
    <div class="email-container">
        <label for="email-address" class="email-label">Email</label>
        <input type="email" name="email_address" id="email-address" class="email-field" placeholder="johnmeyer87@gmail.com" bind:value={email_address} required/>
    </div>
    <div class="country-code-container">
        <label for="country-code" class="country-code-label">Country Code</label>
        <select name="country_code" id="country-code" class="country-code-field" bind:value={country_code}>
            {#each countries as country}
                <option value={country['dial_code']} label={`${country['name']} (${country['dial_code']})`} data-country-name={country['name']} data-country-code={country['code']} data-dial-code={country['dial_code']}></option>
            {/each}
        </select>
    </div>
    <div class="mobile-num-container">
        <label for="mobile-number" class="mobile-num-label">Phone</label>
        <input type="tel" pattern={phone_reg} name="mobile_number" id="mobile-number" class="mobile-num-field" placeholder="XXX-XXX-XXXX" bind:value={mobile_num}/>
    </div>
    <div class="message-container">
        <label for="message" class="message-label">Message</label>
        <textarea id="message" rows="5" name="message" class="message-field" placeholder="Your message here" bind:value={message} required></textarea>
    </div>
    <div class="model-name-container">
        <label for="model-name" class="model-name-label">Model Name</label>
        <select name="model_name" id="model-name" class="model-name-field" bind:value={model_name}>
            {#each model_names as model_name}
                <option value={model_name} label={model_name}></option>
            {/each}
        </select>
    </div>
    <div class="prompt-container">
        <label for="prompt" class="prompt-label">Prompt</label>
        <input bind:value={prompt} id="prompt" class="prompt-field" type="text" placeholder="Type a prompt e.g. Dostoevsky"/>
    </div>
    <div class="temp-container">
        <label for="temp" class="temp-label">Temperature</label>
        <input bind:value={temperature} type="range" min={0.0} max={2.0} step={0.01} id="field" class="temp-field"/>
    </div>
    <div class="seq-len-container">
        <label for="seq-len" class="seq-len-label">Sequence Length</label>
        <input bind:value={seq_len} type="number" id="seq-len" class="seq-len-field" placeholder="250"/>
    </div>
    <div class="image-upload-container">
        <label for="image-upload" class="image-upload-label">Image</label>
        <input type="file" id="image-upload" class="image-upload-field" bind:files={images}>
        
        <!-- when image is uploaded images becomes are not null anymore
        but when another upload occurs and is cancelled images becomes
        a list of length 0 -->
        <img class="uploaded-image" src={images != null ? images.length != 0 ? URL.createObjectURL(images[0]) : null : null} alt="">
    </div>

    <button type="submit" class="submit-btn">Submit</button>
</form>