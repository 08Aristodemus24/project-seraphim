<script>
    let message = "";
</script>

<div class="message-container">
    <label for="message" class="message-label">Message</label>
    <textarea id="message" rows="5" name="message" class="message-field" placeholder="Your message here" bind:value={message} required></textarea>
</div>