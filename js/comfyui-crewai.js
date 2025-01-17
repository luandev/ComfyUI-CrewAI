import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";



app.registerExtension({
  name: "Comfy.CrewAI",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    nodeType.prototype.onNodeCreated = function () {
      // Handles list type inputs
      if (this.type.startsWith("📎CrewAI") && this.type.includes("List")) {
        this.onConnectionsChange = (type, index, connected, linkInfo, ioSlot) => {
          console.log(`\n\n📎`, { type, index, connected, linkInfo, ioSlot });
          const [propName, propIndex] = ioSlot.name.split("-");
          if (!isNaN(propIndex)) {
            if (this.inputs.every((item) => item.link != undefined)) {
              this.addInput(`${propName}-${parseInt(propIndex) + 1}`, ioSlot.type);
            }

            if (!connected && this.inputs.length > 0) {
              const inputIndex = this.inputs.findIndex((item) => item.name === ioSlot.name);
              this.removeInput(inputIndex);
            }

            this.inputs.forEach((item, index) => {
              item.name = `${propName}-${index + 1}`;
            });
          }
        };
      }

      // Handles text display
      if (this.type === "📎CrewAI Text") {
        this.onExecuted = (message) => {
          const callback = (value) => {
            console.log(`📎 Text output changed`, value);
          }
          console.log(`📎 Text Node Executed`, message);
          const text = Array.isArray(message.text) ? message.text.join("\n") : message.text || "";

          let outputWidget = [...this.widgets].find((widget) => widget.name === "output");
          if (!outputWidget) {
            outputWidget = this.addWidget("customtext", `output`, text, callback, { multiline: true })
          }
          outputWidget.value = text;
        };

      }
    };
  },
});
