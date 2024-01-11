<script>
    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";

    let prompt = "";
</script>

<div class={`prompt-container ${style}`} style:--primary-color={primary_color} style:--secondary-color={secondary_color} style:--tertiary-color={tertiary_color}>
    <label for="prompt" class="prompt-label">Prompt</label>
    <input bind:value={prompt} id="prompt" class="prompt-field" type="text" placeholder="Type a prompt e.g. Dostoevsky"/>
</div>

<style>
    .sharp-minimal .prompt-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .prompt-label{
        /* design */
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .sharp-minimal .prompt-field{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .prompt-field{
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
</style>