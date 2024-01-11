<script>
    let temperature = 1.0;
</script>

<div class="temp-container">
    <label for="temp" class="temp-label">Temperature</label>
    <input bind:value={temperature} type="range" min={0.0} max={2.0} step={0.01} id="field" class="temp-field"/>
</div>