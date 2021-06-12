$(document).ready(function() {
  console.log(action);
  switch (action) {
		case 1:
			$("input[name=action1]").prop("checked", true);
      $("input[value=Первичный]").prop("checked", true);
			break;
		case 2:
			$("input[name=action1]").prop("checked", true);
      $("input[value=Повторный]").prop("checked", true);
			break;
		case 3:
			$("input[name=action2]").prop("checked", true);
			break;
		case 4:
			$("input[name=action3]").prop("checked", true);
			break;
		case 5:
			$("input[name=action4]").prop("checked", true);
			break;
		case 6:
			$("input[name=action5]").prop("checked", true);
			break;
		case 7:
			$("input[name=action6]").prop("checked", true);
			break;
	}
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
