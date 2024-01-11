<script>
    export let style = "sharp-minimal";
    export let primary_color = "white";
    export let secondary_color = "black";
    export let tertiary_color = "rgba(255, 255, 255, 0.267)";

    let email_address = "";
</script>

<div class={`email-container ${style}`} style:--primary-color={primary_color} style:--secondary-color={secondary_color} style:--tertiary-color={tertiary_color}>
    <label for="email-address" class="email-label">Email</label>
    <input type="email" name="email_address" id="email-address" class="email-field" placeholder="johnmeyer87@gmail.com" bind:value={email_address} required/>
</div>

<style>
    .sharp-minimal .email-label{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .email-label{
        /* design */
        font-weight: 300;
        font-size: clamp(12px, 1vw, 1rem);
        color: var(--primary-color);

        /* spacing */
        margin-block: 1em;

        /* display */
        display: block;
    }

    .sharp-minimal .email-field{
        /* design */
        font-family: 'Nunito Sans', sans-serif;
    }

    .email-field{
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
    .email-field::placeholder{
        color: var(--tertiary-color);
        opacity: 1; /* Firefox */
    }

    /* Internet Explorer 10-11 */
    .email-field:-ms-input-placeholder{
        color: var(--tertiary-color);
    }

    /* Microsoft Edge */
    .email-field::-ms-input-placeholder{
        color: var(--tertiary-color);
    }
</style>