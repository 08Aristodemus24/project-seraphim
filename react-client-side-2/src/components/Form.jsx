import NameInput from "./NameInput";
import EmailInput from './EmailInput';
import MobileNumberInput from './MobileNumberInput';
import CountryCodeInput from './CountryCodeInput';
// import MessageInput from './MessageInput';
// import ModelNameInput from './ModelNameInput';
// import PromptInput from './PromptInput';
// import SequenceLengthInput from './SequenceLengthInput';
// import TemperatureInput from './TemperatureInput';
// import ImageInput from './ImageInput';
// import Button from "./Button";

import { useContext, useState } from "react";
import { ThemeContext } from "../contexts/ThemeContext";
import { DesignsContext } from "../contexts/DesignsContext";
import { FormInputsContext } from "../contexts/FormInputsContext";


export default function Form(){
    let [fname, setFname] = useState("");
    let [lname, setLname] = useState("");
    let [email, setEmail] = useState("");
    let [mobileNum, setMobileNum] = useState("");
    let [countryCode, setCountryCode] = useState("");

    let style;
    const designs = useContext(DesignsContext);
    const themes = useContext(ThemeContext);
    const { design, theme } = themes;
    
    // sometimes themes context will contain only the design 
    // and not the theme key so check if theme key is in themes
    if('theme' in themes){
        style = designs[design][theme];
    }else{
        style = designs[design];
    }

    // const handleSubmit = async (event) => {
    //     event.preventDefault();
    //     const form_data = new FormData();
    //     form_data.append('first_name', first_name);
    //     form_data.append('last_name', last_name);
    //     form_data.append('email_address', email_address);
    //     form_data.append('country_code', country_code);
    //     form_data.append('mobile_num', mobile_num);
    //     form_data.append('message', message);
    //     form_data.append('model_name', model_name);
    //     form_data.append('prompt', prompt);
    //     form_data.append('seq_len', seq_len);
    //     form_data.append('temperature', temperature);
    //     form_data.append('image', image);
    //     for(var pair of form_data.entries()) {
    //         console.log(pair[0]+', '+pair[1]);
    //     }
    // };
    console.log(`first name: ${fname}`);
    console.log(`last name: ${lname}`);
    console.log(`email: ${email}`);
    console.log(`mobile number: ${mobileNum}`);
    console.log(`country code: ${countryCode}`);

    return (
        <FormInputsContext.Provider value={{fname, setFname, lname, setLname, email, setEmail, mobileNum, setMobileNum, countryCode, setCountryCode}}>
            <div className="form-container">
                <form
                    className={`form ${design}`}
                    style={style}
                    method="POST"
                >
                    <NameInput name-type="first"/>
                    <NameInput name-type="last"/>
                    <EmailInput/>
                    <MobileNumberInput/>
                    <CountryCodeInput/>
                    {/* <MessageInput/>
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