<script>
    import { afterUpdate } from "svelte";

    let images = null;

    afterUpdate(async () => {
        console.log(images);
    });
</script>

<div class="image-upload-container">
    <!-- when image is uploaded images becomes are not null anymore
    but when another upload occurs and is cancelled images becomes
    a list of length 0 -->
    <img class="uploaded-image" src={images != null ? images.length != 0 ? URL.createObjectURL(images[0]) : null : null} alt="">
    <div class="image-upload-field-wrapper">
        <label for="image-upload" class="image-upload-label">Image</label>
        <input type="file" id="image-upload" class="image-upload-field" bind:files={images}>
    </div>
</div>