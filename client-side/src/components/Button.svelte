<script>
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
</script>

<button 
    type="submit" 
    class={`submit-btn ${style}`} 
    style:--primary-color={palette[theme].primary_color} 
    style:--secondary-color={palette[theme].secondary_color} 
    style:--tertiary-color={palette[theme].tertiary_color}
>
    Submit
</button>

<style>
    .submit-btn.sharp-minimal{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
        background-color: transparent;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        border: none;
        outline: 1px solid var(--primary-color);
        
        /* size */
        padding: .5em 5em;

        /* alignment */
        justify-self: center;

        /* animation */
        transition-property: background-color, color;
        transition-duration: 250ms, 250ms;
        transition-timing-function: ease-in-out, ease-in-out;
    }

    .submit-btn.sharp-minimal:hover{
        /* design */
        cursor: pointer;
        background-color: var(--primary-color);
        color: var(--secondary-color);
        outline: 1px solid var(--primary-color);
    }

    .submit-btn.neomorphic{
        /* design */
        
        background-color: transparent;
        box-shadow: 
            12px 12px 16px 0 rgba(0, 0, 0, 0.25),
            -8px -8px 12px 0 rgba(255, 255, 255, 0.507);
        
        font-family: 'Nunito Sans', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        border-radius: 50px;
        border: none;

        /* size */
        padding: .5em 5em;

        /* alignment */
        justify-self: center;
    }
</style>