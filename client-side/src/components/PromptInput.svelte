<script>
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
                secondary_color: "black",
                tertiary_color: "rgba(255, 255, 255, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)"
            },
            light: {
                primary_color: "black",
                secondary_color: "rgb(210, 210, 210)",
                tertiary_color: "rgba(0, 0, 0, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)"
            }
        }
    };

    let prompt = "";
</script>

<div class={`prompt-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <label for="prompt" class="prompt-label">Prompt</label>
    <input bind:value={prompt} id="prompt" class="prompt-field" type="text" placeholder="Type a prompt e.g. Dostoevsky"/>
</div>

<style>
    .sharp-minimal .prompt-label{
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

    .sharp-minimal .prompt-field{
        /* design */
        background-color: transparent;
        color: var(--primary-color);
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

    .sharp-minimal .prompt-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .sharp-minimal .prompt-field:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .sharp-minimal .prompt-field::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .neomorphic.prompt-container{
        /* design */
        background-color: rgb(210, 210, 210);

        /* size */
        padding: 1em;
    }

    .neomorphic .prompt-label{
        /* design */
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        background-color: var(--secondary-color);
        /* outline: 1px solid brown; */

        /* spacing */
        margin-block: 1em;
    
        /* display */
        display: block;
    }

    .neomorphic .prompt-field{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        box-shadow: 
            inset 3px 3px 7px 0 var(--primary-shadow),
            inset -3px -3px 7px 0 var(--secondary-shadow);
        border-radius: 50px;
        border: none;

        /* size */
        width: 12rem;
        padding: 0.5em 1em;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    .neomorphic .prompt-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .neomorphic .prompt-field:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .neomorphic .prompt-field::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }
</style>