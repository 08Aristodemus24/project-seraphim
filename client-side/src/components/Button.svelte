<script>
    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";
</script>

<button 
    type="submit" 
    class={`submit-btn ${style}`} 
    style:--primary-color={primary_color} 
    style:--secondary-color={secondary_color} 
    style:--tertiary-color={tertiary_color}
>Submit</button>

<style>
    .sharp-minimal.submit-btn{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .soft-minimal.submit-btn{
        /* design */
        font-family: 'Poppins', sans-serif;

        /* size */
        border-radius: 10px;
    }

    .submit-btn{
        /* design */
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

    .submit-btn:hover{
        /* design */
        cursor: pointer;
        background-color: var(--primary-color);
        color: var(--secondary-color);
        outline: 1px solid var(--primary-color);
    }    
</style>