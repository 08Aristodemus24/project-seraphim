<script>
    import { onMount } from "svelte";

    export let style = "sharp-minimal";
    export let theme = "dark";

    $:palette = {
        dark: {
            primary_color: "white",
            secondary_color: "black",
            tertiary_color: "rgba(255, 255, 255, 0.267)"    
        },
        light: {
            primary_color: "black",
            secondary_color: "white",
            tertiary_color: "rgba(0, 0, 0, 0.267)"    
        }
    };

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

<div class={`model-name-container ${style}`} style:--primary-color={palette[theme].primary_color} style:--secondary-color={palette[theme].secondary_color} style:--tertiary-color={palette[theme].tertiary_color}>
    <label for="model-name" class="model-name-label">Model Name</label>
    <select name="model_name" id="model-name" class="model-name-field" bind:value={model_name}>
        {#each model_names as model_name}
            <option value={model_name} label={model_name}></option>
        {/each}
    </select>
</div>

<style>
    .sharp-minimal .model-name-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .model-name-label{
        /* design */
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .sharp-minimal .model-name-field{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .model-name-field{
        /* design */
        background-color: transparent;
        color: var(--primary-color);
        font-size: clamp(12px, 1vw, 1rem);
        border-top: none;
        border-right: none;
        border-left: none;
        border-bottom: 1px solid var(--primary-color);

        width: 12rem;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    .model-name-field option{
        /* design */
        background-color: rgba(255, 0, 0, 0);
        color: black;
    }
</style>