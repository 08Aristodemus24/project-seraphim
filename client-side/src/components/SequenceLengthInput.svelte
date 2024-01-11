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

    let seq_len = 250;
</script>

<div class={`seq-len-container ${style}`} style:--primary-color={palette[theme].primary_color} style:--secondary-color={palette[theme].secondary_color} style:--tertiary-color={palette[theme].tertiary_color}>
    <label for="seq-len" class="seq-len-label">Sequence Length</label>
    <input bind:value={seq_len} type="number" id="seq-len" class="seq-len-field" min={0.0} placeholder="250"/>
</div>

<style>
    .sharp-minimal .seq-len-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .seq-len-label{
        /* design */
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .sharp-minimal .seq-len-field{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .seq-len-field{
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