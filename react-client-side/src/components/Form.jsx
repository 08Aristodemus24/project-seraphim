import NameInput from "./NameInput";
// import EmailInput from './EmailInput.svelte';
// import MobileNumberInput from './MobileNumberInput.svelte';
// import CountryCodeInput from './CountryCodeInput.svelte';
// import MessageInput from './MessageInput.svelte';
// import ModelNameInput from './ModelNameInput.svelte';
// import PromptInput from './PromptInput.svelte';
// import SequenceLengthInput from './SequenceLengthInput.svelte';
// import TemperatureInput from './TemperatureInput.svelte';
// import ImageInput from './ImageInput.svelte';
// import Button from "./Button.svelte";

import { useContext, useState } from "react";
import { ThemeContext } from "../contexts/ThemeContext";
import { DesignsContext } from "../contexts/DesignsContext";
import { FormInputsContext } from "../contexts/FormInputsContext";


export default function Form(){
    let [fname, setFname] = useState();
    let [lname, setlname] = useState();
    let [email, setEmail] = useState();

    let style;
    const designs = useContext(DesignsContext);
    if('theme' in useContext(ThemeContext)){
        const { design, theme } = useContext(ThemeContext);
        style = designs[design][theme];
    }else{
        const { design } = useContext(ThemeContext);
        style = designs[design];
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
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
    };

    return (
        <FormInputsContext.Provider value={{fname, setFname, lname, setlname, email, setEmail, handleSubmit}}>
            <div class="form-container">
                <form
                    class={`form ${style}`}
                    style={style}
                    method="POST"
                >
                    <NameInput name_type="first"/>
                    <NameInput name_type="last"/>
                    {/* <EmailInput/>
                    <MobileNumberInput/>
                    <CountryCodeInput/>
                    <MessageInput/>
                    <ModelNameInput/>
                    <PromptInput/>
                    <SequenceLengthInput/>
                    <TemperatureInput/>
                    <ImageInput/>
                    <Button/> */}
                </form>
            </div>
        </FormInputsContext.Provider>
    );
}

const palette = {
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