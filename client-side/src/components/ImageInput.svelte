<script>
    import { afterUpdate } from "svelte";

    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";

    let images = null;

    afterUpdate(async () => {
        console.log(images);
    });
</script>

<div class={`image-upload-container ${style}`} style:--primary-color={primary_color} style:--secondary-color={secondary_color} style:--tertiary-color={tertiary_color}>
    <!-- when image is uploaded images becomes are not null anymore
    but when another upload occurs and is cancelled images becomes
    a list of length 0 -->
    <img class="uploaded-image" src={images != null ? images.length != 0 ? URL.createObjectURL(images[0]) : null : null} alt="">
    <div class="image-upload-field-wrapper">
        <label for="image-upload" class="image-upload-label">Image</label>
        <input type="file" id="image-upload" class="image-upload-field" bind:files={images}>
    </div>
</div>

<style>
    .image-upload-container{
        /* design */
        /* outline: 1px solid red; */

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

    .uploaded-image{
        /* design */
        outline: 1px dashed var(--primary-color);
        outline-offset: 5px;

        /* size */
        height: 200px;
        width: 200px;

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
    }

    .soft-minimal .image-upload-label{
        /* design */
        font-family: 'Poppins', sans-serif;
    }

    .image-upload-label{
        /* design */
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
        font-family: 'Nunito Sans', sans-serif;
    }

    .soft-minimal .image-upload-field{
        /* design */
        font-family: 'Poppins', sans-serif;
    }

    .image-upload-field{
        /* design */
        background-color: transparent;
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
        font-family: 'Nunito Sans', sans-serif;
    }

    .soft-minimal .image-upload-field::-webkit-file-upload-button{
        /* design */
        font-family: 'Poppins', sans-serif;

        /* size */
        border-radius: 10px;
    }

    .image-upload-field::-webkit-file-upload-button{
        /* design */
        color: var(--primary-color);
        background-color: transparent;
        cursor: pointer;
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

    .image-upload-field::-webkit-file-upload-button:hover{
        /* design */
        background-color: var(--primary-color);
        color: var(--secondary-color);
    }
</style>