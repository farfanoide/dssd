(function () {
  try {
    return angular.module('bonitasoft.ui.widgets');
  } catch(e) {
    return angular.module('bonitasoft.ui.widgets', []);
  }
})().directive('pbLink', function() {
    return {
      template: '<div class="text-{{ properties.alignment }}">\n  <a ng-class="properties.buttonStyle !== \'none\' ? \'btn btn-\' + properties.buttonStyle : \'\'" ng-href="{{properties.targetUrl}}" target="{{properties.target}}" ng-bind-html="properties.text | uiTranslate"></a>\n</div>\n'
    };
  });
