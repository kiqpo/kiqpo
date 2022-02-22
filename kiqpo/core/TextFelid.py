def TextFelid(label="",helperText="",characterCounter=False,prefixText=""):
    return f"""<label class="mdc-text-field mdc-text-field--outlined">
  <span class="mdc-notched-outline">
    <span class="mdc-notched-outline__leading"></span>
    <span class="mdc-notched-outline__notch">
      <span class="mdc-floating-label" id="my-label-id">{label}</span>
    </span>
    <span class="mdc-notched-outline__trailing"></span>
  </span>
  <input type="text" class="mdc-text-field__input" aria-labelledby="my-label-id">
</label>
<div class="mdc-text-field-helper-line">
  <div class="mdc-text-field-helper-text" id="my-helper-id" aria-hidden="true">
  {helperText}
  </div>"""