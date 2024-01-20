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

    export let mobile_num;
    const phone_reg = `[0-9]{'{'}3{'}'}-[0-9]{'{'}3{'}'}-[0-9]{'{'}4{'}'}`;
</script>

<div class={`mobile-num-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <label for="mobile-number" class="mobile-num-label">Phone</label>
    <input type="tel" pattern={phone_reg} name="mobile_number" id="mobile-number" class={`mobile-num-field ${style}`} placeholder="XXX-XXX-XXXX" bind:value={mobile_num}/>
</div>

<style>
    .sharp-minimal .mobile-num-label{
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

    .sharp-minimal .mobile-num-field{
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
    .sharp-minimal .mobile-num-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1; /* Firefox */
    }

    /* Internet Explorer 10-11 */
    .sharp-minimal .mobile-num-field:-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* Microsoft Edge */
    .sharp-minimal .mobile-num-field::-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    .light-neomorphic.mobile-num-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }
    
    .light-neomorphic .mobile-num-label{
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

    .light-neomorphic .mobile-num-field{
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

    .light-neomorphic .mobile-num-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .light-neomorphic .mobile-num-field:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .light-neomorphic .mobile-num-field::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .dark-neomorphic.mobile-num-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .dark-neomorphic .mobile-num-label{
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

    .dark-neomorphic .mobile-num-field{
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

    .dark-neomorphic .mobile-num-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .dark-neomorphic .mobile-num-field:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .dark-neomorphic .mobile-num-field::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }
</style>