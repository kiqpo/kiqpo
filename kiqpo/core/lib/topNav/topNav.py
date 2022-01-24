def topNav(label="",labelgap="0.7%", backgroundColor="#2c9bff", height="57px", icon=False, iconPath="./src/icon.png"):
    if icon == True:
        return f"""<div style="
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  top:0px;
  left:0px;
  width: 100vw;
  height: {height};
  background: {backgroundColor};
  box-shadow: rgba(50, 50, 93, 0.151) 0px 13px 27px -5px,
  rgba(0, 0, 0, 0.233) 0px 8px 16px -8px;">
  <img style="width: 3rem;
  margin-top: 7px;" src="{iconPath}" alt="bard-logo">
</div>"""
    else:
        return f"""<div style="
  position: absolute;
  top:0px;
  left:0px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 100vw;
  z-index:1000;
  height: {height};
  background: {backgroundColor};
  box-shadow: rgba(50, 50, 93, 0.151) 0px 13px 27px -5px,
  rgba(0, 0, 0, 0.233) 0px 8px 16px -8px;">
  <div style='padding:{labelgap};' >
        {label}
  </div>
</div>
<div style='position: relative;
  width: 100vw;
  top:0%;
  left:0%;
  height: {height};
  background-color: {backgroundColor};'>
</div>"""
