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
            primary_color: "rgb(38,39,43)",
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

    let first_name = "";
    let last_name = "";
    let email_address = "";
    let country_code = "";
    let mobile_num = "";
    let message = "";

    const handle_submit = (event) => {
        console.log('hello');
        const data = {
            first_name: first_name,
            last_name: last_name,
            email_address: email_address,
            country_code: country_code,
            mobile_num: mobile_num,
            message: message
        };

        dispatch('sendData', data);
    };

    
</script>

<div class="form-container">
    <form 
        class={`form ${style}`}
        style:--primary-color={palette[theme].primary_color} 
        style:--secondary-color={palette[theme].secondary_color} 
        style:--tertiary-color={palette[theme].tertiary_color}
        on:submit={handle_submit}
        bind:this={form}
        method="POST" 
    >
        <NameInput name_type="first" style="dark-neomorphic" theme="dark" name={first_name}/>
        <NameInput name_type="last" style="dark-neomorphic" theme="dark" name={last_name}/>
        <EmailInput style="dark-neomorphic" theme="dark" email_address={email_address}/>
        <MobileNumberInput style="dark-neomorphic" theme="dark" mobile_num={mobile_num}/>
        <CountryCodeInput style="dark-neomorphic" theme="dark" country_code={country_code}/>
        <MessageInput style="dark-neomorphic" theme="dark" message={message}/>
        <ModelNameInput style="dark-neomorphic" theme="dark"/>
        <PromptInput style="dark-neomorphic" theme="dark"/>
        <SequenceLengthInput style="dark-neomorphic" theme="dark"/>
        <TemperatureInput style="dark-neomorphic" theme="dark"/>
        <ImageInput style="dark-neomorphic" theme="dark"/>
        <Button style="dark-neomorphic" theme="dark"/>
        <button type="submit">test</button>
    </form>
</div>

<style>
    .form-container{
        /* design */
        outline: 1px solid yellow;

        /* size */
        /* width: 100%; */

        /* spacing */
        margin-block: 1rem;
    }

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