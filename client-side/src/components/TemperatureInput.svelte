<script>
    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";

    let temperature = 1.0;
</script>

<div class={`temp-container ${style}`} style:--primary-color={primary_color} style:--secondary-color={secondary_color} style:--tertiary-color={tertiary_color}>
    <label for="temp" class="temp-label">Temperature</label>
    <input bind:value={temperature} type="range" min={0.0} max={2.0} step={0.01} id="field" class="temp-field"/>
</div>

<style>
    .sharp-minimal .temp-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .temp-label{
        /* design */
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);
        /* outline: 1px solid brown; */

        /* spacing */
        margin-block: 1em;
    
        /* display */
        display: block;
    }

    .temp-field{
        /* size */
        width: 12rem;
        /* width: 30rem; */

        /* design */
        background-color: var(--primary-color);
        -webkit-appearance: none;
    }

    .temp-field::-webkit-slider-runnable-track{
        /* size */
        height: 0.5px;

        /* design */
        cursor: pointer;
        border-radius: 0px;
        border: 0px solid black;
        box-shadow: none;
        appearance: none;
    }

    .temp-field::-ms-track{
        /* size */
        height: 1px;

        /* design */
        cursor: pointer;
        border-radius: 0px;
        border: 0px solid black;
        box-shadow: none;
        appearance: none;
    }

    .temp-field::-webkit-slider-thumb{
        /* size */
        height: 20px;
        width: 3px;

        /* design */
        box-shadow: none;
        border: 0px solid black;
        background-color: var(--primary-color);
        cursor: pointer;
        margin-top: -10px;
        -webkit-appearance: none;
    }

    .temp-field::-ms-thumb{
        /* size */
        height: 20px;
        width: 3px;

        /* design */
        box-shadow: none;
        border: 0px solid black;
        background-color: var(--primary-color);
        cursor: pointer;
        margin-top: -10px;
        -webkit-appearance: none;
    }
</style>