<script>
    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";

    let mobile_num = "";
    const phone_reg = `[0-9]{'{'}3{'}'}-[0-9]{'{'}3{'}'}-[0-9]{'{'}4{'}'}`;
</script>

<div class={`mobile-num-container ${style}`} style:--primary-color={primary_color} style:--secondary-color={secondary_color} style:--tertiary-color={tertiary_color}>
    <label for="mobile-number" class="mobile-num-label">Phone</label>
    <input type="tel" pattern={phone_reg} name="mobile_number" id="mobile-number" class="mobile-num-field" placeholder="XXX-XXX-XXXX" bind:value={mobile_num}/>
</div>

<style>
    .sharp-minimal .mobile-num-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .mobile-num-label{
        /* design */
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .sharp-minimal .mobile-num-field{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .mobile-num-field{
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

    /* Chrome, Firefox, Opera, Safari 10.1+ */
    .mobile-num-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1; /* Firefox */
    }

    /* Internet Explorer 10-11 */
    .mobile-num-field:-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* Microsoft Edge */
    .mobile-num-field::-ms-input-placeholder{
        color: var(--tertiary-color);
    }
</style>