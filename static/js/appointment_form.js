$(document).ready(function() {
  locstor = window.localStorage;
  $("input[name=name]").val(locstor.getItem("name"));
  $("input[name=age]").val(locstor.getItem("age"));
  $("input[name=phone]").val(locstor.getItem("phone"));
  if(locstor.getItem("destination")) $(`input[name=destination][value=${locstor.getItem("destination")}]`).prop("checked", true);
  $("input[name=action1]").prop("checked", Boolean(Number(locstor.getItem("action1"))));
  $("input[name=action2]").prop("checked", Boolean(Number(locstor.getItem("action2"))));
  $("input[name=action3]").prop("checked", Boolean(Number(locstor.getItem("action3"))));
  $("input[name=action4]").prop("checked", Boolean(Number(locstor.getItem("action4"))));
  $("input[name=action5]").prop("checked", Boolean(Number(locstor.getItem("action5"))));
  $("input[name=action6]").prop("checked", Boolean(Number(locstor.getItem("action6"))));

  switch (action) {
		case 1:
			$("input[name=action1]").prop("checked", true);
      locstor.setItem("action1", 1);
      $("input[value=Первичный]").prop("checked", true);
			break;
		case 2:
			$("input[name=action1]").prop("checked", true);
      locstor.setItem("action1", 1);
      $("input[value=Повторный]").prop("checked", true);
			break;
		case 3:
			$("input[name=action2]").prop("checked", true);
      locstor.setItem("action2", 1);
			break;
		case 4:
			$("input[name=action3]").prop("checked", true);
      locstor.setItem("action3", 1);
			break;
		case 5:
			$("input[name=action4]").prop("checked", true);
      locstor.setItem("action4", 1);
			break;
		case 6:
			$("input[name=action5]").prop("checked", true);
      locstor.setItem("action5", 1);
			break;
		case 7:
			$("input[name=action6]").prop("checked", true);
      locstor.setItem("action6", 1);
			break;
	}



  for(let i = 1; i <= 6; i++) {
    $(`span[name=action${i}`).bind("click", function() {
      let target = $(`input[name=action${i}]`);
      if (target.is(":checked")) {
        target.prop("checked", false);
        locstor.setItem(`action${i}`, 0);
      } else {
        target.prop("checked", true);
        locstor.setItem(`action${i}`, 1);
      }
    });
  }

  $("input[name=name]").bind("input", function() {
    locstor.setItem("name", $(this).val());
  });
  $("input[name=age]").bind("input", function() {
    locstor.setItem("age", $(this).val());
  });
  $("input[name=phone]").bind("input", function() {
    locstor.setItem("phone", $(this).val());
  });
  $("input[name=destination]").bind("input", function() {
    locstor.setItem("destination", $(this).val());
  });
  $("input[name=action1]").bind("input", function() {
    locstor.setItem("action1", Number($(this).is(":checked")));
  });
  $("input[name=action2]").bind("input", function() {
    locstor.setItem("action2", Number($(this).is(":checked")));
  });
  $("input[name=action3]").bind("input", function() {
    locstor.setItem("action3", Number($(this).is(":checked")));
  });
  $("input[name=action4]").bind("input", function() {
    locstor.setItem("action4", Number($(this).is(":checked")));
  });
  $("input[name=action5]").bind("input", function() {
    locstor.setItem("action5", Number($(this).is(":checked")));
  });
  $("input[name=action6]").bind("input", function() {
    locstor.setItem("action6", Number($(this).is(":checked")));
  });

});
