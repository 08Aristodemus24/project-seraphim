import Section from './components/Section';
import { Form } from './components/Form';
import { Alert } from './components/Alert';

export default function Correspondence(){
    // pass this state as props to Form component
    // so that it gets binded to the form element
    let form;
    let alert_container;

    // response state
    let response;
    let msg_status;
    let error_type = null;

    const send_data = async (event) => {
        try {
            // extract data from form element
            const raw_data = event.detail;

            // once data is validated submitted and then extracted
            // reset form components form element
            form.reset();

            // send here the data from the contact component to 
            // the backend proxy server
            // // for development
            const url = 'http://127.0.0.1:5000/send-data';
            // for production
            // const url = 'https://project-alexander.vercel.app/send-data';

            response = await fetch(url, {
                'method': 'POST',
                'body': raw_data,
            });

            // if response.status is 200 then that means contact information
            // has been successfully sent to the email.js api
            if(response.status === 200){
                msg_status = "success";
                console.log(`message has been sent with code ${response.status}`);

            }else{
                msg_status = "failure";
                console.log(`message submission unsucessful. Response status '${response.status}' occured`);
            }

        }catch(error){
            msg_status = "denied";
            error_type = error;
            console.log(`Submission denied. Error '${error}' occured`);
        }
    };
    
    return (
        <Section section-name={"data-form"}>
            <Form/>
            <Alert/>
        </Section>
    )
}