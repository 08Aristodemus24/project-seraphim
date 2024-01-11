<script>
    export let name_type;
    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";
    
    let name_code = name_type === 'first' ? 'f' : 'l';
    let placeholder = name_type === 'first' ? 'John Smith' : 'Meyer';
    let name;
    

    const capitalize = (string) => string[0].toUpperCase() + string.substring(1);
</script>

<div class={`${name_code}name-container ${style}`} style:--primary-color={primary_color} style:--secondary-color={secondary_color} style:--tertiary-color={tertiary_color}>
    <label for="last-name" class={`${name_code}name-label`}>{`${capitalize(name_type)} name`}</label>
    <input type="text" name={`${name_type}_name`} id={`${name_type}-name`} class={`${name_code}name-field`} placeholder={placeholder} bind:value={name}/>
</div>

<style>
    .sharp-minimal label[class*="name-label"]{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    label[class*="name-label"]{
        /* design */
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
    }

    input[class*="name-field"]{
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

    /* Chrome, Firefox, Opera, Safari 10.1+ */
    input[class*="name-field"]::placeholder{
        color: var(--tertiary-color);
        opacity: 1; /* Firefox */
    }

    /* Internet Explorer 10-11 */
    input[class*="name-field"]:-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* Microsoft Edge */
    input[class*="name-field"]::-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* what properties can change? And are dynamic */
</style>