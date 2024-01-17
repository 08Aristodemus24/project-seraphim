<script>
    import { onMount } from "svelte";

    export let style = "sharp-minimal";
    export let theme = "dark";

    $:palette = {
        'sharp-minimal':{
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
        },
        'light-neomorphic': {
            light: {
                primary_color: "black",
                secondary_color: "rgb(231, 238, 246)",
                tertiary_color: "rgba(0, 0, 0, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)"
            }
        },
        'dark-neomorphic': {
            dark: {
                primary_color: "rgb(231, 238, 246)",
                secondary_color: "rgb(38,39,43)",
                tertiary_color: "rgba(255, 255, 255, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(210, 210, 210, 0.5)"
            },
        }
    };

    let model_names = ['------------------------'];
    export let model_name;

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

<div class={`model-name-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <label for="model-name" class="model-name-label">Model Name</label>
    <select name="model_name" id="model-name" class={`model-name-field ${style}`} bind:value={model_name}>
        {#each model_names as model_name}
            <option value={model_name} label={model_name}></option>
        {/each}
    </select>
</div>

<style>
    .sharp-minimal .model-name-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
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
        color: var(--primary-color);
        background-color: transparent;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
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

    .sharp-minimal .model-name-field option{
        /* design */
        background-color: rgba(255, 0, 0, 0);
        color: black;
    }

    .light-neomorphic.model-name-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .light-neomorphic .model-name-label{
        /* design */
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .light-neomorphic .model-name-field{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        box-shadow:
            3px 3px 8px 0 var(--primary-shadow),
            -3px -3px 8px 0 var(--secondary-shadow);;
        border-radius: 10px;
        border: none;

        /* size */
        width: 12rem;
        padding: 0.5em 1em;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    .light-neomorphic .model-name-field option{
        /* design */
        background-color: rgba(255, 0, 0, 0);
        color: black;
    }

    .dark-neomorphic.model-name-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .dark-neomorphic .model-name-label{
        /* design */
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .dark-neomorphic .model-name-field{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        box-shadow: 
            3px 7px 8px 0 var(--primary-shadow),
            -2px -2px 8px -3px var(--secondary-shadow);

        /* box-shadow: 
            3px 2px 8px 1px var(--primary-shadow),
            -2px -1.5px 5px -1px var(--secondary-shadow); */
        border-radius: 10px;
        border: none;

        /* size */
        width: 12rem;
        padding: 0.5em 1em;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    .dark-neomorphic .model-name-field option{
        /* design */
        background-color: rgba(255, 0, 0, 0);
        color: black;
    }
</style>