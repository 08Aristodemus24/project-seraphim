<script>
    export let style = "sharp-minimal";
    export let theme = "dark";

    // $:palette = {
    //     'sharp-minimal':{
    //         dark: {
    //             primary_color: "white",
    //             secondary_color: "black",
    //             tertiary_color: "rgba(255, 255, 255, 0.267)"    
    //         },
    //         light: {
    //             primary_color: "black",
    //             secondary_color: "white",
    //             tertiary_color: "rgba(0, 0, 0, 0.267)"
    //         }
    //     },
    //     'neomorphic': {
    //         dark: {
    //             primary_color: "white",
    //             secondary_color: "rgb(38,39,43)",
    //             tertiary_color: "rgba(255, 255, 255, 0.267)",
    //             primary_shadow: "rgba(0, 0, 0, 0.25)",
    //             secondary_shadow: "rgba(255, 255, 255, 0.5)"
    //         },
    //         light: {
    //             primary_color: "black",
    //             secondary_color: "rgb(231, 238, 246)",
    //             tertiary_color: "rgba(0, 0, 0, 0.267)",
    //             primary_shadow: "rgba(0, 0, 0, 0.25)",
    //             secondary_shadow: "rgba(255, 255, 255, 0.5)"
    //         }
    //     }
    // };

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

    $:toggler = style.includes('neomorphic') ? (event) => {
        if(event.target.classList.contains('clicked')){
            console.log('closed');
            event.target.classList.remove('clicked');
        }else{
            console.log('added');
            event.target.classList.add('clicked');
        }
    } : null;
</script>

<div 
    class={`submit-btn-container ${style}`}
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}
>
    <button type="submit" class={`submit-btn ${style}`} on:mousedown={toggler} on:mouseup={toggler} on:click|preventDefault>
        Submit
    </button>
</div>


<style>
    .sharp-minimal .submit-btn{
        /* design */
        background-color: transparent;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
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

    .sharp-minimal .submit-btn:hover{
        /* design */
        cursor: pointer;
        background-color: var(--primary-color);
        color: var(--secondary-color);
    }

    .light-neomorphic.submit-btn-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .light-neomorphic .submit-btn{
        /* design */
        background-color: var(--secondary-color);
        box-shadow: 
            3px 3px 8px 0 var(--primary-shadow),
            -10px -10px 15px 0 var(--secondary-shadow);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        color: var(--primary-color);
        border-radius: 50px;
        border: none;

        /* size */
        padding: .5em 5em;  

        /* alignment */
        justify-self: center;
    }

    .light-neomorphic.submit-btn.clicked{
        /* design */
        box-shadow: 
            inset 3px 3px 7px 0 var(--primary-shadow),
            inset -3px -3px 7px 0 var(--secondary-shadow);
    }

    .dark-neomorphic.submit-btn-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .dark-neomorphic .submit-btn{
        /* design */
        background-color: var(--secondary-color);
        box-shadow: 
            3px 7px 8px 0 var(--primary-shadow),
            -2px -2px 8px 0 var(--secondary-shadow);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        color: var(--primary-color);
        border-radius: 50px;
        border: none;

        /* size */
        padding: .5em 5em;  

        /* alignment */
        justify-self: center;
    }

    .dark-neomorphic.submit-btn.clicked{
        /* design */
        box-shadow: 
            inset 3px 7px 8px 0 var(--primary-shadow),
            inset -2px -2px 5px 0 var(--secondary-shadow);
    }
</style>