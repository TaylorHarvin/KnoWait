<?php
	class NeuralNetwork{
		public $inToHidWeights = array();
	   	public $hidNodes = array();
	    public $hidToOutWeights = array();
	    public $outNodes = array();
	    public $outDeltas = array();
	    public $hidDeltas = array();
	    public $prevInToHidChange = array();
	    public $prevHidToOutChange = array();
	    public $inputNodeSize = 0;


		public function __construct($inputNodeSize, $hiddenNodeSize,$outputNodeSize, $prevInToOtherWeights, $prevHidToOutWeights){
			$this->hidNodes = array_fill(0,$hiddenNodeSize,0);
        	$this->outNodes = array_fill(0,$outputNodeSize,0);
        	$this->outDeltas = array_fill(0,$outputNodeSize,0);
        	$this->hidDeltas = array_fill(0,$hiddenNodeSize,0);
        	$this->prevInToHidChange = array_fill(0,$inputNodeSize*$hiddenNodeSize,0);
        	$this->prevHidToOutChange = array_fill(0,$hiddenNodeSize*$outputNodeSize,0);
        	$this->inputNodeSize = $inputNodeSize;


        	if($hiddenNodeSize <= 0){
	            if(sizeof($prevInToOtherWeights) > 0)
	            	$this->inToOutWeights = $prevInToOtherWeights;
	            else
	            	$this->inToOutWeights = $inputNodeSize*$outputNodeSize;
	           
	            $prevInToOutChange = $nputNodeSize*$outputNodeSize;
	        }
	        else{
	           if(sizeof($prevInToOtherWeights) > 0 and sizeof($prevHidToOutWeights) > 0){
	               $this->inToHidWeights = $prevInToOtherWeights;
	               $this->hidToOutWeights = $prevHidToOutWeights;
	            }
	               
	           else{
	               $this->hidToOutWeights =$hiddenNodeSize*$outputNodeSize;
	               $this->inToHidWeights =$inputNodeSize*$hiddenNodeSize;
	            }
	        }
		               
	        if(sizeof($prevInToOtherWeights) <= 0 and sizeof($prevHidToOutWeights) <= 0){
	        	$this->refresh();
	        }

	        
		}

		public function refresh(){
	        for($index = 0; $index < sizeof($this->inToHidWeights); $index++){
	            $this->inToHidWeights[$index] = rand();
	            #self.inToHidWeights[index] = 0.1
	        }
	        for($index = 0; $index < sizeof($this->hidToOutWeights); $index++){
	            $this->hidToOutWeights[$index] = rand();
	        }
	    }


	}


	srand(0);

	$nn = new NeuralNetwork(5,4,1,[],[]);

	print(sizeof($nn->inToHidWeights));

?>