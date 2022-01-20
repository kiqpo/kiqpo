def topNav(labelText="Kiqpo", backgroundColor="#2c9bff", height="57px", labelFontSize="1.7rem", icon=False, iconPath="./src/icon.png"):
    if icon == True:
        return f"""<div style="
  position: absolute;
  top:0px;
  left:0px;
  width: 100vw;
  height: {height};
  background: {backgroundColor};
  box-shadow: rgba(50, 50, 93, 0.151) 0px 13px 27px -5px,
  rgba(0, 0, 0, 0.233) 0px 8px 16px -8px;">
  <img style="width: 3rem;
  margin-top: 7px;
  margin-left: 5%;" src="{iconPath}" alt="bard-logo">
</div>"""
    else:
        return f"""<div style="
  position: absolute;
  top:0px;
  left:0px;
  width: 100vw;
  height: {height};
  background: {backgroundColor};
  box-shadow: rgba(50, 50, 93, 0.151) 0px 13px 27px -5px,
  rgba(0, 0, 0, 0.233) 0px 8px 16px -8px;">
      <h2  style="margin-left: 5%;
  margin-top: 10px;
  font-size: {labelFontSize};
  font-family: Arial, Helvetica, sans-serif;">{labelText}</h2>
</div>"""
