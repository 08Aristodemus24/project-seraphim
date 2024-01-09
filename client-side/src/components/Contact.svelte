<script>
    import Form from "./Form.svelte";

    // pass this state as props to Form component
    // so that it gets binded to the form element
    let form;
    let alert_container;

    // response state
    let response;
    let msg_status;
    let error_type = null;

    const send_mail = async (event) => {
        try {
            // extract data from form element
            const raw_data = event.detail;

            // once data is validated submitted and then extracted
            // reset form components form element
            form.reset();

            // send here the data from the contact component to 
            // the backend proxy server
            // // for development
            // const url = 'http://127.0.0.1:5000/send-mail';
            // for production
            const url = 'https://project-alexander.vercel.app/send-mail';

            response = await fetch(url, {
                'method': 'POST',
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': JSON.stringify(raw_data)
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
</script>

<section id="contact-section">
    <div class="contact-content">
        <div class="contact-header-container">
            <h1>Send me a message</h1>
        </div>
        <div class="form-container">
            <Form on:sendMail={send_mail} bind:form/>
        </div>
    </div>
    <div class="alert-container" class:show={msg_status !== undefined} on:click={(event) => {
        // remove class from alert container to hide it again
        event.target.classList.remove('show');

        // reset msg_status to undefined in case of another submission
        msg_status = undefined;
    }}>
        <div class="alert-wrapper">
            {#if msg_status === "success" || msg_status === "failed"}
                <span class="alert">Message has been sent with code {response?.status}</span>    
            {:else}
                <span class="alert">Submission denied. Error '{error_type}'' occured</span>
            {/if}
        </div>
    </div>
</section>