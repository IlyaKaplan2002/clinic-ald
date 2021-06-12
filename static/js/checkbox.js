$(document).ready(function() {
  for(let i = 1; i <= 6; i++) {
    $(`span[name=action${i}`).bind("click", function() {
      let target = $(`input[name=action${i}]`);
      if (target.is(":checked")) {
        target.prop("checked", false);
      } else {
        target.prop("checked", true);
      }
    });
  }
});
