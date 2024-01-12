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
                secondary_color: "white",
                tertiary_color: "rgba(0, 0, 0, 0.267)",
                primary_shadow: "rgba(0, 0, 0, 0.25)",
                secondary_shadow: "rgba(255, 255, 255, 0.5)"
            }
        }
    };
</script>

<button 
    type="submit"
    class={`submit-btn ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
    on:click|preventDefault={(event) => {
        if(event.target.classList.contains('clicked')){
            event.target.classList.remove('clicked');
        }else{
            event.target.classList.add('clicked');
        }
    }}
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
            12px 12px 24px 0 var(--primary-shadow),
            -12px -12px 24px 0 var(--secondary-shadow);
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

    .submit-btn.neomorphic.clicked{
        /* design */
        box-shadow: 
            inset 3px 3px 7px 0 var(--primary-shadow),
            inset -3px -3px 7px 0 var(--secondary-shadow);
    }
</style>