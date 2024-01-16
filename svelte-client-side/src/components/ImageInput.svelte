<script>
    import { afterUpdate } from "svelte";

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

    $:toggler = style.includes('neomorphic') ? (event) => {
        console.log(event.target.classList);
        if(event.target.classList.contains('clicked')){
            event.target.classList.remove('clicked');
        }else{
            event.target.classList.add('clicked');
        }
    } : null;

    export let images = null;

    afterUpdate(async () => {
        console.log(images);
    });
</script>

<div 
    class={`image-upload-container ${style}`} 
    style:--primary-color={palette[style][theme].primary_color} 
    style:--secondary-color={palette[style][theme].secondary_color} 
    style:--tertiary-color={palette[style][theme].tertiary_color}
    style:--primary-shadow={palette[style][theme].primary_shadow}
    style:--secondary-shadow={palette[style][theme].secondary_shadow}    
>
    <!-- when image is uploaded images becomes are not null anymore
    but when another upload occurs and is cancelled images becomes
    a list of length 0 -->
    <img class={`uploaded-image ${style}`} src={images != null ? images.length != 0 ? URL.createObjectURL(images[0]) : null : null} alt=" ">
    <div class="image-upload-field-wrapper">
        <label for="image-upload" class="image-upload-label">Image</label>    
        <input type="file" id="image-upload" class={`image-upload-field ${style}`} bind:files={images} on:mousedown={toggler} on:mouseup={toggler}>
    </div>
</div>

<style>
    .image-upload-container{
        /* design */
        outline: 1px solid red;

        /* display */
        display: flex;
        align-items: flex-start;
        justify-content: center;
        flex-direction: column;
        gap: 2rem;

        /* spacing */
        /* put padding of 5px since outlien offset 
        of 5px for image is specified */
        padding: 5px;
    }

    .sharp-minimal .uploaded-image{
        /* design */
        outline: 1px dashed var(--primary-color);
        outline-offset: 5px;

        /* size */
        height: 200px;
        width: 200px;

        /* display */
        display: block;
    }

    .light-neomorphic .uploaded-image{
        /* design */
        background-color: var(--secondary-color);
        box-shadow: 
            inset 3px 3px 7px 0 var(--primary-shadow),
            inset -3px -3px 7px 0 var(--secondary-shadow);
        border-radius: 20px;

        /* size */
        height: 200px;
        width: 200px;

        /* display */
        display: block;
    }

    .dark-neomorphic .uploaded-image{
        /* design */
        background-color: var(--secondary-color);
        box-shadow: 
            inset 3px 7px 8px 0 var(--primary-shadow),
            inset -2px -2px 5px 0 var(--secondary-shadow);
        border-radius: 20px;
        outline: 1px solid rebeccapurple;

        /* size */
        height: 500px;
        width: 500px;

        /* display */
        display: block;
    }

    .image-upload-field-wrapper{
        /* design */
        /* outline: 1px solid var(--primary-color); */

        /* display */
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .sharp-minimal .image-upload-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        /* outline: 1px solid yellow; */

        /* spacing */
        margin-block: 1em;
    
        /* display */
        display: block;
    }

    .sharp-minimal .image-upload-field{
        /* design */
        background-color: transparent;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        text-align: center;
        /* outline: 1px solid greenyellow; */
    
        /* display */
        display: flex;

        /* size */
        padding: 0.5em;
    }

    .sharp-minimal .image-upload-field::-webkit-file-upload-button{
        /* design */
        color: var(--primary-color);
        background-color: transparent;
        cursor: pointer;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        -webkit-user-select: none;
        
        /* size */
        border: 1px solid var(--primary-color);
        padding: .5em 1.5em;
        margin-right: 2.5rem;
        
        /* display */
        display: inline-block;

        /* transition */
        transition-property: background-color, color;
        transition-duration: 250ms, 250ms;
        transition-timing-function: ease-in-out, ease-in-out;
    }

    .sharp-minimal .image-upload-field::-webkit-file-upload-button:hover{
        /* design */
        background-color: var(--primary-color);
        color: var(--secondary-color);
    }

    .light-neomorphic.image-upload-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .light-neomorphic .image-upload-label{
        /* design */
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        /* outline: 1px solid yellow; */

        /* spacing */
        margin-block: 1em;
    
        /* display */
        display: block;
    }

    .light-neomorphic .image-upload-field{
        /* design */
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        color: var(--primary-color);
        text-align: center;
        /* outline: 1px solid greenyellow; */
    
        /* display */
        display: flex;

        /* size */
        padding: 1em;
    }

    .light-neomorphic .image-upload-field::-webkit-file-upload-button{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        box-shadow: 
            3px 3px 8px 0 var(--primary-shadow),
            -3px -3px 8px 0 var(--secondary-shadow);
        border-radius: 50px;
        cursor: pointer;
        font-weight: 300;
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        -webkit-user-select: none;
        
        /* size */
        border: none;
        padding: .5em 1.5em;
        margin-right: 2.5rem;
        
        /* display */
        display: inline-block;

        /* transition */
        transition-property: background-color, color;
        transition-duration: 250ms, 250ms;
        transition-timing-function: ease-in-out, ease-in-out;
    }

    .light-neomorphic.image-upload-field.clicked::-webkit-file-upload-button{
        /* design */
        box-shadow: 
            inset 3px 3px 7px 0 var(--primary-shadow),
            inset -3px -3px 7px 0 var(--secondary-shadow);
    }

    .dark-neomorphic.image-upload-container{
        /* design */
        background-color: var(--secondary-color);

        /* size */
        padding: 1em;
    }

    .dark-neomorphic .image-upload-label{
        /* design */
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        /* outline: 1px solid yellow; */

        /* spacing */
        margin-block: 1em;
    
        /* display */
        display: block;
    }

    .dark-neomorphic .image-upload-field{
        /* design */
        background-color: var(--secondary-color);
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        font-weight: 300;
        color: var(--primary-color);
        text-align: center;
        /* outline: 1px solid greenyellow; */
    
        /* display */
        display: flex;

        /* size */
        padding: 1em;
    }

    .dark-neomorphic .image-upload-field::-webkit-file-upload-button{
        /* design */
        color: var(--primary-color);
        background-color: var(--secondary-color);
        box-shadow: 
            3px 7px 8px 0 var(--primary-shadow),
            -2px -2px 8px 0 var(--secondary-shadow);
        border-radius: 50px;
        cursor: pointer;
        font-weight: 300;
        font-family: 'Poppins', sans-serif;
        font-size: clamp(12px, 1vw, 1rem);
        -webkit-user-select: none;
        
        /* size */
        border: none;
        padding: .5em 1.5em;
        margin-right: 2.5rem;
        
        /* display */
        display: inline-block;

        /* transition */
        transition-property: background-color, color;
        transition-duration: 250ms, 250ms;
        transition-timing-function: ease-in-out, ease-in-out;
    }

    .dark-neomorphic.image-upload-field.clicked::-webkit-file-upload-button{
        /* design */
        box-shadow: 
            inset 3px 7px 8px 0 var(--primary-shadow),
            inset -2px -2px 5px 0 var(--secondary-shadow);
    }
</style>