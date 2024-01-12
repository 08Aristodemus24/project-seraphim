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
    
    export let style = "sharp-minimal";
    export let theme = "dark";

    $:palette = {
        dark: {
            primary_color: "black",
            secondary_color: "white",
            tertiary_color: "rgba(0, 0, 0, 0.267)"    
        },
        light: {
            primary_color: "rgb(231, 238, 246)",
            secondary_color: "black",
            tertiary_color: "rgba(255, 255, 255, 0.267)"    
        }
    };

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

<form 
    class={`form ${style}`}
    style:--primary-color={palette[theme].primary_color} 
    style:--secondary-color={palette[theme].secondary_color} 
    style:--tertiary-color={palette[theme].tertiary_color}
    on:submit|preventDefault={handle_submit} 
    method="post" 
    bind:this={form}
>
    <NameInput name_type="first" style="neomorphic" theme="light"/>
    <NameInput name_type="last" style="neomorphic" theme="light"/>
    <EmailInput style="neomorphic" theme="light"/>
    <MobileNumberInput style="neomorphic" theme="light"/>
    <CountryCodeInput style="neomorphic" theme="light"/>
    <MessageInput style="neomorphic" theme="light"/>
    <ModelNameInput style="neomorphic" theme="light"/>
    <PromptInput style="neomorphic" theme="light"/>
    <SequenceLengthInput style="neomorphic" theme="light"/>
    <TemperatureInput style="neomorphic" theme="light"/>
    <ImageInput style="neomorphic" theme="light"/>
    <Button style="neomorphic" theme="light"/>
</form>

<style>
    .form{
        /* display */
        display: flex;
        align-items: center;
        flex-direction: column;
        gap: 1rem;

        /* size */
        padding: 5px;

        /* design */
        /* outline: 2px solid red; */
        background-color: var(--primary-color);
    }
</style>