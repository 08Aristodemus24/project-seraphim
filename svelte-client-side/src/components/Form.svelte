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
    let model_name = "";
    let prompt = "";
    let seq_len = "250";
    let temperature = "1.0";
    let image = null;

    const handle_submit = async () => {
        const form_data = new FormData();
        form_data.append('first_name', first_name);
        form_data.append('last_name', last_name);
        form_data.append('email_address', email_address);
        form_data.append('country_code', country_code);
        form_data.append('mobile_num', mobile_num);
        form_data.append('message', message);
        form_data.append('model_name', model_name);
        form_data.append('prompt', prompt);
        form_data.append('seq_len', seq_len);
        form_data.append('temperature', temperature);
        form_data.append('image', image);
        for(var pair of form_data.entries()) {
            console.log(pair[0]+', '+pair[1]);
        }
        dispatch('sendData', form_data);
    };

    afterUpdate(() => {
        console.log(image);
    })

    
</script>

<div class="form-container">
    <form
        class={`form ${style}`}
        style:--primary-color={palette[theme].primary_color} 
        style:--secondary-color={palette[theme].secondary_color} 
        style:--tertiary-color={palette[theme].tertiary_color}
        on:submit|preventDefault={handle_submit}
        bind:this={form}
        method="post" 
    >
        <NameInput name_type="first" style="light-neomorphic" theme="light" bind:name={first_name}/>
        <NameInput name_type="last" style="light-neomorphic" theme="light" bind:name={last_name}/>
        <EmailInput style="light-neomorphic" theme="light" bind:email_address={email_address}/>
        <MobileNumberInput style="light-neomorphic" theme="light" bind:mobile_num={mobile_num}/>
        <CountryCodeInput style="light-neomorphic" theme="light" bind:country_code={country_code}/>
        <MessageInput style="light-neomorphic" theme="light" bind:message={message}/>
        <ModelNameInput style="light-neomorphic" theme="light" bind:model_name={model_name}/>
        <PromptInput style="light-neomorphic" theme="light" bind:prompt={prompt}/>
        <SequenceLengthInput style="light-neomorphic" theme="light" bind:seq_len={seq_len}/>
        <TemperatureInput style="light-neomorphic" theme="light" bind:temperature={temperature}/>
        <ImageInput style="light-neomorphic" theme="light" bind:image={image}/>
        <Button style="light-neomorphic" theme="light"/>
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