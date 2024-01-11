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
    <NameInput name_type="first"/>
    <NameInput name_type="last"/>
    <EmailInput/>
    <CountryCodeInput/>
    <MessageInput/>
    <ModelNameInput/>
    <PromptInput/>
    <SequenceLengthInput/>
    <TemperatureInput/>
    <ImageInput/>
    <button type="submit" class="submit-btn">Submit</button>
</form>