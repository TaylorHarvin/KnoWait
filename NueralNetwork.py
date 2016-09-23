#!C:\Python35\python.exe
import random
import math
import time

class NueralNetwork:
    #inNodes = []
    inToHidWeights =[]
    hidNodes = []
    hidToOutWeights = []
    outNodes = []
    outDeltas = []
    hidDeltas = []
    prevInToHidChange = []
    prevHidToOutChange = []
    inputNodeSize = 0

    def __init__(self, inputNodeSize, hiddenNodeSize,outputNodeSize):
        #self.inNodes =[0.0]*inputNodeSize;
        self.inToHidWeights =[0.0]*inputNodeSize*hiddenNodeSize
        self.hidNodes =[0.0]*hiddenNodeSize
        self.hidToOutWeights =[0.0]*hiddenNodeSize*outputNodeSize
        self.outNodes =[0.0]*outputNodeSize
        self.outDeltas = [0.0]*outputNodeSize
        self.hidDeltas = [0.0]*hiddenNodeSize
        self.prevInToHidChange = [0.0]*inputNodeSize*hiddenNodeSize
        self.prevHidToOutChange = [0.0]*hiddenNodeSize*outputNodeSize
        self.inputNodeSize = inputNodeSize
        
    def refresh(self):
        for index in range(len(self.inToHidWeights)):
            self.inToHidWeights[index] = random.random()
            #self.inToHidWeights[index] = 0.1
        for index in range(len(self.hidToOutWeights)):
            self.hidToOutWeights[index] = random.random()
            '''if(index == 1):
                self.hidToOutWeights[index] = 0.1
            else:
                self.hidToOutWeights[index] = 0.2'''

    def activate(self,val):
        return 1.0/(1.0+math.pow(math.e,(-1.0)*val))
    
    def activateDeriv(self,val):
        return self.activate(val)*(1.0 - self.activate(val))

    def normalize(self, val, low, high, targetLow, targetHigh):
        numer = (val-low)*(targetHigh - targetLow)
        denom = (high - low)
        return (numer/denom)
      
    def processInput(self, newInputNodes):
        if(len(self.hidNodes) > 0):
            for hidNodeIndex in range(len(self.hidNodes)):
                self.hidNodes[hidNodeIndex] = 0
                for inNodeIndex in range(len(newInputNodes)):
                    #print((hidNodeIndex*inNodeIndex) + inNodeIndex%len(newInputNodes))
                    self.hidNodes[hidNodeIndex] += newInputNodes[inNodeIndex] * self.inToHidWeights[(hidNodeIndex*len(newInputNodes)) + inNodeIndex]
                self.hidNodes[hidNodeIndex] = self.activate(self.hidNodes[hidNodeIndex]);
                
            for outNodeIndex in range(len(self.outNodes)):
                self.outNodes[outNodeIndex] = 0
                for hidNodeIndex in range(len(self.hidNodes)):
                    #print((outNodeIndex*len(self.hidNodes)) + hidNodeIndex)
                    self.outNodes[outNodeIndex] += self.hidNodes[hidNodeIndex] * self.hidToOutWeights[(outNodeIndex*len(self.hidNodes)) + hidNodeIndex]
                self.outNodes[outNodeIndex] = self.activate(self.outNodes[outNodeIndex]);

    def ApplyWeightChange(self, learningRate, momentumRate):
        inToHidIndex = 0
        hidToOutIndex = 0
        for hidNodeIndex in range(len(self.hidNodes)):
            for outNodeIndex in range(len(self.outNodes)):
                hidToInIndex = hidNodeIndex + (outNodeIndex*len(self.hidNodes))
                self.prevHidToOutChange[hidToOutIndex] = learningRate*self.outDeltas[outNodeIndex] + momentumRate*self.prevHidToOutChange[hidToOutIndex]
                self.hidToOutWeights[hidToOutIndex] += self.prevHidToOutChange[hidToOutIndex]
                
        for inNodeIndex in range(self.inputNodeSize):
            for hidNodeIndex in range(len(self.hidNodes)):
                inToHidIndex = inNodeIndex + (hidNodeIndex*self.inputNodeSize)
                self.prevInToHidChange[inToHidIndex] = learningRate*self.hidDeltas[hidNodeIndex] + momentumRate*self.prevInToHidChange[inToHidIndex]
                self.inToHidWeights[inToHidIndex] += self.prevInToHidChange[inToHidIndex]


    def train(self, inputNodes, expectedOutputNodes, learningRate, momentumRate):
        nn.processInput(inputNodes);
        #Calculate output deltas
        for outNodeIndex in range(len(self.outDeltas)):
            self.outDeltas[outNodeIndex] = (expectedOutputNodes[outNodeIndex] - self.outNodes[outNodeIndex])*self.activateDeriv(self.outNodes[outNodeIndex])

        for hidNodeIndex in range(len(self.hidNodes)):
            self.hidDeltas[hidNodeIndex] = 0
            for outNodeIndex in range(len(self.outNodes)):
                #print(hidNodeIndex + (outNodeIndex*len(self.hidNodes)))
                self.hidDeltas[hidNodeIndex] += self.outDeltas[outNodeIndex] * self.hidToOutWeights[hidNodeIndex + (outNodeIndex*len(self.hidNodes))]
            #print("\n")
        self.ApplyWeightChange(learningRate,momentumRate);    

random.seed(0)
#nn = NueralNetwork(4,3,1)
nn = NueralNetwork(4,3,2)
nn.refresh()
for i in range(1000):
    nn.train([0.5,0.4,0.5,0.6],[0.1,0.8],0.2,0.8)
    #time.sleep(0.5)
nn.processInput([0.5,0.4,0.5,0.6]);
print(nn.outNodes)

