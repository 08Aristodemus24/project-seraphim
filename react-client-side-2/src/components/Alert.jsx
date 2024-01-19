export default function Alert({ 'msg-status': msg_status, 'error-type': error_type, response }){

    return (
        <div class="alert-container" class:show={msg_status !== undefined} on:click={(event) => {
            // remove class from alert container to hide it again
            event.target.classList.remove('show');
        
            // reset msg_status to undefined in case of another submission
            msg_status = undefined;
        }}>
            <div class="alert-wrapper">
                {msg_status === "success" || msg_status === "failed" ? 
                <span class="alert">Message has been sent with code {response?.status}</span> : 
                <span class="alert">Submission denied. Error '{error_type}'' occured</span>}
            </div>
        </div>
    );
}