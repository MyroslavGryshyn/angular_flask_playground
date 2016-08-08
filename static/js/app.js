var app = angular.module('homeworkApp', ['ngResource']);

app.factory('Vacancy', function($resource) {
  return $resource('/api/vacs/:id');
});

app.directive('allVacancies', function($resource, Vacancy) {
    return {
      templateUrl: 'static/js/all.html',
      controller: function() {
        var vacancies = this;
        var vacs = Vacancy.query(function() {
          vacancies.vacancies = vacs;
          console.log(vacancies.vacancies);
        });
      },
      controllerAs: 'vacancies'
    };
  });

app.directive('oneVacancy', function($resource, Vacancy) {
    return {
      templateUrl: 'static/js/one.html',
      controller: function() {
        var vacancy = this;
        var vac = Vacancy.get({id: 2}, function() {
          vacancy.data = vac;
        });
      },
      controllerAs: 'vacancy'
    };
  });
