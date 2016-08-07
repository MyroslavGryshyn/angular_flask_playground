var app = angular.module('homeworkApp', []);

app.directive('allVacancies', function() {
    return {
      templateUrl: 'static/js/all.html',
      controller: function($http) {
        var vacancy = this;
        $http.get('api/1').then(
        function(response) {
          vacancy.data = response.data;
        });
      },
      controllerAs: 'vacancy'
    };
  });
