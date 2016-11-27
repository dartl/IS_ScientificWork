$(window).load(function () {

  /* Обработка выбора типа публикации в фильтре на странице Публикаций */
  last_type = "";
  $("[name='typePublication']").change(function() {
    console.log($(this).val());
    if ($(this).val() == '') {
      $(".filter .display-none").hide(300);
    }

    if ($(this).val() == "guidelines") {
      $(".filter .display-none").hide(300);
      $("[name='type']").parent().show(300);
      $("[name='isbn']").parent().show(300);
    }

    if ($(this).val() == "book") {
      if (last_type != "guidelines") {
        $(".filter .display-none").hide(300);
        $("[name='type']").parent().show(300);
        $("[name='isbn']").parent().show(300);
      }
    }

    if ($(this).val() == "journal") {
      $(".filter .display-none").hide(300);
      $("[name='number']").parent().show(300);
    }

    if ($(this).val() == "compilation") {
      if (last_type == "guidelines" || last_type == "book" ) {
        $("[name='type']").parent().hide(300);
      } else {
        $(".filter .display-none").hide(300);
        $("[name='isbn']").parent().show(300);
      }
      
    }

    if ($(this).val() == "collection") {
      if (last_type != "journal") {
        $(".filter .display-none").hide(300);
      }
      $("[name='number']").parent().show(300);
      $("[name='editor']").parent().show(300);
      $("[name='reiteration']").parent().show(300);
    }
    last_type = $(this).val();
  });
});