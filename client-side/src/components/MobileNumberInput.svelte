<script>
    let mobile_num = "";
    const phone_reg = `[0-9]{'{'}3{'}'}-[0-9]{'{'}3{'}'}-[0-9]{'{'}4{'}'}`;
</script>

<div class="mobile-num-container">
    <label for="mobile-number" class="mobile-num-label">Phone</label>
    <input type="tel" pattern={phone_reg} name="mobile_number" id="mobile-number" class="mobile-num-field" placeholder="XXX-XXX-XXXX" bind:value={mobile_num}/>
</div>