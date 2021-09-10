const assert = require('assert');
const Math = require('../src/math.js');
const expect = require('chai').expect;

describe('Math class', function(){
	beforeEach(function() {
        //o que fazer após cada teste        
    });
    
    it('soma dois números', function(done) {
        this.timeout(3000);

		const math = new Math();
        const operacao = () => math.sum(1, 1);
        const resultadoEsperado = 2;

        assert.equal(operacao(), resultadoEsperado);
        done();
	});

    it('multiplicar dois números', function() {
        const math = new Math();
        const operacao = () => math.mult(5, 2);
        const resultadoEsperado = 5 * 2;

        assert.equal(operacao(), resultadoEsperado);


        expect(operacao()).to.equal(10)
    });

    it.skip('dividir dois números', function() {
        const math = new Math();
        const operacao = () => math.div(5, 2);
        const resultadoEsperado = 5 * 2;

        assert.equal(operacao(), resultadoEsperado);
    });
});