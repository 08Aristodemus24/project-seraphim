<script>
    export let style = "sharp-minimal";
    export let theme = "dark";

    $:palette = {
        'sharp-minimal':{
            dark: {
                primary_color: "white",
                secondary_color: "black",
                tertiary_color: "rgba(255, 255, 255, 0.267)",
                primary_background: "black",
            },
            light: {
                primary_color: "black",
                secondary_color: "white",
                tertiary_color: "rgba(0, 0, 0, 0.267)",
                primary_background: "white",
            }
        },
        'light-neomorphic': {
            light: {
                primary_color: "black",
                secondary_color: "rgb(231, 238, 246)",
                tertiary_color: "rgba(0, 0, 0, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)",
                primary_background: "rgb(231, 238, 246)",
            }
        },
        'dark-neomorphic': {
            dark: {
                primary_color: "rgb(231, 238, 246)",
                secondary_color: "rgb(38, 39, 43)",
                tertiary_color: "rgba(255, 255, 255, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(210, 210, 210, 0.5)",
                primary_background: "rgb(38, 39, 43)",
            },
        }
    };

    export let email_address;
</script>

<div class={`email-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <label for="email-address" class="email-label">Email</label>
    <input type="email" name="email_address" id="email-address" class={`email-field ${style}`} placeholder="johnmeyer87@gmail.com" bind:value={email_address} required/>
</div>

<style>
    .sharp-minimal .email-label{
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

    .sharp-minimal .email-field{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        background-color: transparent;
        color: var(--primary-color);
        border-top: none;
        border-right: none;
        border-left: none;
        border-bottom: 1px solid var(--primary-color);

        width: 12rem;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    /* Chrome, Firefox, Opera, Safari 10.1+ */
    .email-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1; /* Firefox */
    }

    /* Internet Explorer 10-11 */
    .email-field:-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* Microsoft Edge */
    .email-field::-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    .light-neomorphic.email-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }
    
    .light-neomorphic .email-label{
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

    .light-neomorphic .email-field{
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

    .light-neomorphic .email-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .light-neomorphic .email-field:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .light-neomorphic .email-field::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .dark-neomorphic.mobile-num-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .dark-neomorphic .email-label{
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

    .dark-neomorphic .email-field{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        box-shadow: 
            inset 3px 7px 8px 0 var(--primary-shadow),
            inset -2px -2px 5px -2px var(--secondary-shadow);
        border-radius: 10px;
        border: none;

        /* size */
        width: 12rem;
        padding: 0.5em 1em;
        /* width: 30rem; */

        /* display */
        display: block;

        /* functionality */
        resize: none;
    }

    .dark-neomorphic .email-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .dark-neomorphic .email-field:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .dark-neomorphic .email-field::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }
</style>