<script>
    import { onMount, onDestroy, createEventDispatcher, afterUpdate } from "svelte";

    import NameInput from './NameInput.svelte';
    import EmailInput from './EmailInput.svelte';
    import MobileNumberInput from './MobileNumberInput.svelte';
    import CountryCodeInput from './CountryCodeInput.svelte';
    import MessageInput from './MessageInput.svelte';
    import ModelNameInput from './ModelNameInput.svelte';
    import PromptInput from './PromptInput.svelte';
    import SequenceLengthInput from './SequenceLengthInput.svelte';
    import TemperatureInput from './TemperatureInput.svelte';
    import ImageInput from './ImageInput.svelte';
    import Button from "./Button.svelte";
    

    // bind the passed state from Contact component to the form
    // element in this Form component
    export let form;
    let dispatch = createEventDispatcher();

    const handle_submit = (event) => {
        const mail = {
            // first_name: first_name,
            // last_name: last_name,
            // email_address: email_address,
            // country_code: country_code,
            // mobile_num: mobile_num,
            // message: message
        };

        dispatch('sendData', mail);
    };

    
</script>

<form class="form one-col" on:submit|preventDefault={handle_submit} method="post" bind:this={form}>
    <NameInput name_type="first" style="sharp-minimal" primary_color="white"/>
    <NameInput name_type="last" style="sharp-minimal" primary_color="white"/>
    <EmailInput primary_color="black" secondary_color="white"/>
    <MobileNumberInput primary_color="black" secondary_color="white"/>
    <CountryCodeInput primary_color="black" secondary_color="white"/>
    <MessageInput primary_color="black" secondary_color="white"/>
    <ModelNameInput primary_color="black" secondary_color="white"/>
    <PromptInput primary_color="black" secondary_color="white"/>
    <SequenceLengthInput primary_color="black" secondary_color="white"/>
    <TemperatureInput primary_color="black" secondary_color="white"/>
    <ImageInput style="soft-minimal" primary_color="black" secondary_color="white"/>
    <Button style="soft-minimal"/>
</form>

<style>
    .form.two-col{
        /* display */
        /* display: grid; */

        /* size of columns and rows */
        /* grid-template-columns: repeat(auto-fit, 1fr); */

        /* alignment */
        /* align-items: center; */

        /* spacing */
        /* row-gap: 2rem;
        column-gap: 1.5rem; */

        /* design */
        /* outline: 2px solid lightgreen; */
    }

    .form.one-col{
        /* display */
        display: flex;
        align-items: center;
        flex-direction: column;
        gap: 1rem;

        /* outline */
        outline: 2px solid lightskyblue;

    }

    .form div[class*="container"]{
        /*  */
        outline: 1px solid salmon;
    }   
</style>