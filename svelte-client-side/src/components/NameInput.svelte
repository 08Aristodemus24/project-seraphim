<script>
    export let name_type;
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
    
    let name_code = name_type === 'first' ? 'f' : 'l';
    let placeholder = name_type === 'first' ? 'John Smith' : 'Meyer';
    export let name;

    const capitalize = (string) => string[0].toUpperCase() + string.substring(1);
</script>

<div class={`${name_code}name-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <label for="last-name" class={`${name_code}name-label`}>{`${capitalize(name_type)} name`}</label>
    <input type="text" name={`${name_type}_name`} id={`${name_type}-name`} class={`${name_code}name-field ${style}`} placeholder={placeholder} bind:value={name}/>
</div>

<style>
    .sharp-minimal label[class*="name-label"]{
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

    .sharp-minimal input[class*="name-field"]{
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
    .sharp-minimal input[class*="name-field"]::placeholder{
        color: var(--tertiary-color);
        opacity: 1; /* Firefox */
    }

    /* Internet Explorer 10-11 */
    .sharp-minimal input[class*="name-field"]:-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* Microsoft Edge */
    .sharp-minimal input[class*="name-field"]::-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    div[class*="name-container"].light-neomorphic{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }
    
    .light-neomorphic label[class*="name-label"]{
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

    .light-neomorphic input[class*="name-field"]{
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

    .light-neomorphic input[class*="name-field"]::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .light-neomorphic input[class*="name-field"]:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .light-neomorphic input[class*="name-field"]::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    div[class*="name-container"].dark-neomorphic{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }
    
    .dark-neomorphic label[class*="name-label"]{
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

    .dark-neomorphic input[class*="name-field"]{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        box-shadow: 
            inset 3px 7px 8px 0 var(--primary-shadow),
            inset -2px -2px 5px -2px var(--secondary-shadow);
        border-radius: 50px;
        border: none;

        /* size */
        width: 12rem;
        padding: 0.5em 1em;
        /* width: 30rem; */

        /* display */
        display: block;
    }

    .dark-neomorphic input[class*="name-field"]::placeholder{
        color: var(--tertiary-color);
        opacity: 1;            
    }

    .dark-neomorphic input[class*="name-field"]:-ms-input-placeholder{
        color: var(--tertiary-color);                
    }

    .dark-neomorphic input[class*="name-field"]::-ms-input-placeholder{
        color: var(--tertiary-color);                
    }
</style>