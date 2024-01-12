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
        'neomorphic': {
            dark: {
                primary_color: "white",
                secondary_color: "rgb(38,39,43)",
                tertiary_color: "rgba(255, 255, 255, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)"
            },
            light: {
                primary_color: "black",
                secondary_color: "rgb(231, 238, 246)",
                tertiary_color: "rgba(0, 0, 0, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)"
            }
        }
    };

    let countries = [];
    let country_code = "";

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

    onMount(async () => {
        get_country_codes();
    });
</script>

<div class={`country-code-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <label for="country-code" class="country-code-label">Country Code</label>
    <select name="country_code" id="country-code" class="country-code-field" bind:value={country_code}>
        {#each countries as country}
            <option value={country['dial_code']} label={`${country['name']} (${country['dial_code']})`} data-country-name={country['name']} data-country-code={country['code']} data-dial-code={country['dial_code']}></option>
        {/each}
    </select>
</div>

<style>
    .sharp-minimal .country-code-label{
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

    .sharp-minimal .country-code-field{
        /* design */
        background-color: transparent;
        color: var(--primary-color);
        font-family: 'Nunito Sans', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        border-top: none;
        border-right: none;
        border-left: none;
        border-bottom: 1px solid var(--primary-color);

        width: 12rem;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    .sharp-minimal .country-code-field option{
        /* design */
        background-color: rgba(255, 0, 0, 0);
        color: black;
    }

    .neomorphic.country-code-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .neomorphic .country-code-label{
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

    .neomorphic .country-code-field{
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
</style>