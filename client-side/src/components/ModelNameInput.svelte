<script>
    import { onMount } from "svelte";

    let model_names = ['------------------------'];
    let model_name = "";

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
        get_model_names();
    });
</script>

<div class="model-name-container">
    <label for="model-name" class="model-name-label">Model Name</label>
    <select name="model_name" id="model-name" class="model-name-field" bind:value={model_name}>
        {#each model_names as model_name}
            <option value={model_name} label={model_name}></option>
        {/each}
    </select>
</div>