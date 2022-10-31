// This model contains school information
import { decimalToPercentString } from '../util/number-utils.js';
import { getStateValue } from '../dispatchers/get-model-values.js';
import { updateState } from '../dispatchers/update-state.js';
import { updateUrlQueryString } from '../dispatchers/update-view.js';

const schoolModel = {
  values: {},

  textPercents: [
    'defaultRate',
    'rateGraduation',
    'rateRepay3yr',
    'rateAssociateTransfer'
  ],

  setValue: function( name, value, updateURL ) {
    schoolModel.values[name] = value;

    if ( schoolModel.textPercents.indexOf( name ) !== -1 ) {
      const key = name + 'Text';
      schoolModel.values[key] = decimalToPercentString( value, 1 );
    }
    // Alert the state model to school control
    if ( name === 'control' ) {
      updateState.byProperty( 'schoolControl', value );
    }

    if ( name === 'highestDegree' ) {
      updateState.byProperty( 'communityCollege', value === 'Associate degree' );
    }

    if ( updateURL !== false ) {
      updateUrlQueryString();
    }
  },

  /**
   * Reformats the programCodes array into an Object keyed by program ID
   */
  createProgramLists: function() {
    schoolModel.values.programList = {};
    if (
      {}.hasOwnProperty.call( schoolModel.values, 'programCodes' ) &&
      schoolModel.values.programCodes !== null
    ) {
      const programCodes = schoolModel.values.programCodes;
      for ( const key in programCodes ) {
        schoolModel.values.programList[key] = {};
        if ( programCodes[key].length > 0 ) {
          programCodes[key].forEach( elem => {
            schoolModel.values.programList[key][elem.code] = {
              name: elem.name,
              level: elem.level,
              salary: elem.salary
            };
          } );
        }
      }
    }
  },

  /**
   * Returns an array of Objects which is alphabetized
   * by program name
   * @param {string} level - program level - 'undergrad' or 'graduate'
   * @returns {array} an array of objects containing program data
   */
  getAlphabeticalProgramList: function( level ) {
    let list = [];
    if ( !{}.hasOwnProperty.call( schoolModel.values, 'programCodes' ) ) return list;
    if ( !{}.hasOwnProperty.call( schoolModel.values.programCodes, level ) ) return list;

    list = schoolModel.values.programCodes[level].sort( ( a, b ) => {
      if ( a.name < b.name ) {
        return -1;
      } else if ( a.name > b.name ) {
        return 1;
      } else if ( b.name === a.name ) {
        if ( a.level < b.level ) return -1;
        else if ( a.level > b.level ) return 1;
      }
      return 0;
    } );

    return list;
  },

  /**
   * getProgramInfo - retrieve info based on program id
   * @param {string} pid - Program ID
   * @returns {object|boolean} Values of the program, or false if undefined
   */
  getProgramInfo: function( pid ) {
    const level = getStateValue( 'programLevel' );
    const hasLevel = level !== null || level !== false;
    const hasProgram = pid !== null || typeof pid !== 'undefined';

    if ( !hasProgram || !hasLevel ) {
      return false;
    } else if (
      !{}.hasOwnProperty.call( schoolModel.values, 'programList' ) ||
      !{}.hasOwnProperty.call( schoolModel.values.programList[level], pid )
    ) {
      return false;
    }

    return schoolModel.values.programList[level][pid];
  }
};

export { schoolModel };
