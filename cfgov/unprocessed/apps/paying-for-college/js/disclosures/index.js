import $ from './utils/dollar-sign.js';
import fetch from './dispatchers/get-api-values.js';
import verifyOffer from './dispatchers/post-verify.js';
import financialModel from './models/financial-model.js';
import schoolModel from './models/school-model.js';
import expensesModel from './models/expenses-model.js';
import getFinancial from './dispatchers/get-financial-values.js';
import getExpenses from './dispatchers/get-expenses-values.js';
import {
  getUrlOfferExists,
  getUrlValues,
} from './dispatchers/get-url-values.js';
import financialView from './views/financial-view.js';
import expensesView from './views/expenses-view.js';
import metricView from './views/metric-view.js';
import questionView from './views/question-view.js';
import publish from './dispatchers/publish-update.js';

// import('./utils/print-page.js');

const ready = function (callback) {
  if (document.readyState !== 'loading') {
    // Document is already ready, call the callback directly
    callback();
  } else if (document.addEventListener) {
    // All modern browsers to register DOMContentLoaded
    document.addEventListener('DOMContentLoaded', callback);
  } else {
    // Old IE browsers
    document.attachEvent('onreadystatechange', function () {
      if (document.readyState === 'complete') {
        callback();
      }
    });
  }
};

const app = {
  urlValues: {},
  init: function () {
    // jquery promise to delay full model creation until ajax resolves
    fetch.initialData().then((resp) => {
      const constants = JSON.parse(resp[0].responseText);
      const expenses = JSON.parse(resp[1].responseText);
      financialModel.init(constants[0]);
      financialView.init();
      if (location.href.indexOf('about-this-tool') === -1) {
        expensesModel.init(expenses);
        expensesView.init();
      }
      if (getUrlOfferExists()) {
        // Check for URL offer data
        this.urlValues = getUrlValues();
        fetch
          .schoolData(this.urlValues.collegeID, this.urlValues.programID)
          .then((respArr) => {
            const schoolData = JSON.parse(respArr[0].responseText);
            const programData = JSON.parse(respArr[1].responseText);
            const nationalData = JSON.parse(respArr[1].responseText);
            const data = {};
            Object.assign(data, schoolData, programData, nationalData);
            const schoolValues = schoolModel.init(
              nationalData,
              schoolData,
              programData,
            );

            /* If PID exists, update the financial model and view based
           on program data */
            if (!{}.hasOwnProperty.call(data, 'pidNotFound')) {
              financialModel.updateModelWithProgram(schoolValues);
              financialView.updateViewWithProgram(schoolValues, this.urlValues);
            }

            // Add url values to the financial model
            publish.extendFinancialData(this.urlValues);
            if (typeof this.urlValues.totalCost === 'undefined') {
              publish.financialData('totalCost', null);
            }
            financialView.updateViewWithURL(schoolValues, this.urlValues);
            // initialize metric view
            metricView.init();
            financialView.updateView(getFinancial.values());
            questionView.init();

            // Update expenses model bases on region and salary
            const region = schoolValues.BLSAverage.substr(0, 2);
            $('#bls-region-select').val(region).change();
          });
      }
      // set financial caps based on data
      financialView.setCaps(getFinancial.values());
      financialView.updateView(getFinancial.values());
    });
    verifyOffer.init();
  },
};

ready(function () {
  app.init();

  /* The following line allows for functional testing by exposing
     the getFinancial method.
     $( '#financial-offer' ).data( 'getFinancial', getFinancial );
     console.log( $( '#financial-offer' ).data() ); */
  window.getFinancial = getFinancial;
  window.getExpenses = getExpenses;
});
