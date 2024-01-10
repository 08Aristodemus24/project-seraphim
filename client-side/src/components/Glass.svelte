<script>
    let prompt = "";
    let temperature = 1.0;
    let seq_len = 250;
</script>
<div class="glass-container">
    <div class="glass">
        <div class="messages-container">
        </div>
        <div class="prompts-container">
            <div class="prompt-group">
                <div class="input-container">
                    <label for="prompt-field" class="prompt-label">prompt: </label>
                    <input bind:value={prompt} id="prompt-field" class="prompt-field" type="text" placeholder="Type a prompt e.g. Dostoevsky"/>
                </div>
                
                <div class="input-container">
                    <label for="temp-field" class="temp-label">temperature: </label>
                    <input bind:value={temperature} type="range" min={0.0} max={2.0} step={0.01} id="temp-field"  class="temp-field"/>
                </div>
                
                <div class="input-container">
                    <label for="seq-len-field" class="seq-len-label">sequence length: </label>
                    <input bind:value={seq_len} type="number" id="seq-len-field" class="seq-len-field" placeholder={`${seq_len}`}/>
                </div>
            </div>

            <button class="generate-btn">generate</button>
        </div>
    </div>
</div>