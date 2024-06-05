import { app } from "../../scripts/app.js"

app.registerExtension({
    name: "Comfy.CrewAI",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        nodeType.prototype.onNodeCreated = function () {
            if (this.type.startsWith("CrewAI")) {
                
                this.onConnectionsChange = (type, index, connected, linkInfo, ioSlot) => {
                    console.log(`\n\n📎`, {type, index, connected, linkInfo, ioSlot})
                    const [propName, propIndex] = ioSlot.name.split('-');
                    if (!isNaN(propIndex)) {
                        console.log(this.inputs.every(item => item.link != undefined));
                        if (this.inputs.every(item => item.link != undefined)) 
                            this.addInput(`${propName}-${parseInt(propIndex) + 1}`, ioSlot.type);

                        if (!connected && this.inputs.length > 0) {
                            const inputIndex = this.inputs.findIndex(item => item.name === ioSlot.name);
                            this.removeInput(inputIndex);
                        }

                        this.inputs.forEach((item, index) => {
                            const [propName] = ioSlot.name.split('-');
                            item.name = `${propName}-${index + 1}`;
                        })
                    }
                };
            }
        };
    },
});
