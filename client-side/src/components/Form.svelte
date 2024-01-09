<script>
    import { onMount, onDestroy, createEventDispatcher } from "svelte";

    // bind the passed state from Contact component to the form
    // element in this Form component
    export let form;

    let countries = [];

    let first_name = "";
    let last_name = "";
    let email_address = "";
    let country_code = "";
    let mobile_num = "";
    let message = "";

    let dispatch = createEventDispatcher();

    onMount(async () => {
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
    });

    const handle_submit = (event) => {
        const mail = {
            first_name: first_name,
            last_name: last_name,
            email_address: email_address,
            country_code: country_code,
            mobile_num: mobile_num,
            message: message
        };

        dispatch('sendMail', mail);
    };

    const phone_reg = `[0-9]{'{'}3{'}'}-[0-9]{'{'}3{'}'}-[0-9]{'{'}4{'}'}`;
</script>

<form class="form" on:submit|preventDefault={handle_submit} method="post" bind:this={form}>
    <div class="fname-container">
        <label for="first-name" class="fname-label">First name</label>
        <input type="text" name="first_name" id="first-name" class="fname-field" placeholder="Larry Miguel" bind:value={first_name}/>
    </div>
    <div class="lname-container">
        <label for="last-name" class="lname-label">Last name</label>
        <input type="text" name="last_name" id="last-name" class="lname-field" placeholder="Cueva" bind:value={last_name}/>
    </div>
    <div class="email-container">
        <label for="email-address" class="email-label">Email</label>
        <input type="email" name="email_address" id="email-address" class="email-field" placeholder="MichaelAveuc571@gmail.com" bind:value={email_address} required/>
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
    <button type="submit" class="submit-btn">Submit</button>
</form>