webpackJsonp([5],{0:function(e,t,r){"use strict";var n=r(1),s=r(142),a=r(270);n.render(s.createElement(a,{url:"/api/v1/groups/",pollInterval:2e4}),document.getElementById("groups_table"))},162:function(e,t,r){"use strict";var n=r(142);e.exports=n.createClass({displayName:"exports",render:function(){if(this.props.item.is_archived)var e="UnArchive";else var e="Archive";return n.createElement("a",{className:"ui tiny grey button",onClick:this.props.archiveFn},e)}})},270:function(e,t,r){(function(t){"use strict";var n=r(142),s=r(271);e.exports=n.createClass({displayName:"exports",archiveGroup:function(e){var r=this;t.ajax({url:"/api/v1/groups/"+e.pk,type:"POST",data:{archive:!0},success:function(e){r.loadResponsesFromServer()},error:function(e,t,r){window.alert("uh, oh. That didn't work."),console.log(e.status+": "+e.responseText)}})},loadResponsesFromServer:function(){t.ajax({url:this.props.url,dataType:"json",success:function(e){this.setState({data:e})}.bind(this),error:function(e,t,r){console.error(this.props.url,t,r.toString())}.bind(this)})},getInitialState:function(){return{data:[]}},componentDidMount:function(){this.loadResponsesFromServer(),setInterval(this.loadResponsesFromServer,this.props.pollInterval)},render:function(){var e=this,t=this.state.data.map(function(t,r){return n.createElement(s,{group:t,key:r,archiveGroup:e.archiveGroup.bind(null,t)})});return n.createElement("table",{className:"ui very basic striped table"},n.createElement("thead",null,n.createElement("tr",null,n.createElement("th",null,"Name"),n.createElement("th",null,"Description"),n.createElement("th",null,"Cost"),n.createElement("th",null))),n.createElement("tbody",{className:"searchable"},t))}})}).call(t,r(155))},271:function(e,t,r){"use strict";var n=r(142),s=r(162);e.exports=n.createClass({displayName:"exports",render:function(){return n.createElement("tr",null,n.createElement("td",null,n.createElement("a",{href:this.props.group.url},this.props.group.name)),n.createElement("td",null,this.props.group.description),n.createElement("td",{className:"collapsing"},"$"+this.props.group.cost),n.createElement("td",{className:"collapsing"},n.createElement(s,{item:this.props.group,archiveFn:this.props.archiveGroup})))}})}});